from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Profile_user
import numpy as np
from PIL import Image
from . import feature_extractor
from pathlib import Path
import numpy as np
import json 
import glob
import pickle
from base64 import b64decode

import os

# Create your views here.
def userregister(request):
    if request.method=='POST':
        user = Profile_user()
        user.first_name =request.POST.get('firstname')
        user.last_name =request.POST.get('lastname')
        user.mail =request.POST.get('email')
        user.age =request.POST.get('age')
        user.profile_pic=request.FILES.get('profile_pic')
        print(user.profile_pic)
        user.save()
        img_name =user.profile_pic
        pickleconverter(img_name)
        
        return render(request,'userregister.html')
    return render(request,'userregister.html')
def pickleconverter(img_name):
        img_path =Path(f"./media/{img_name}")
        fe = feature_extractor.FeatureExtractor()

        print(img_path)  # e.g., ./static/img/xxx.jpg
        feature = fe.extract(img=Image.open(img_path))
        feature_path = Path("./media/feature") / (img_path.stem + ".npy")  # e.g., ./static/feature/xxx.npy
        np.save(feature_path, feature)


def verify_image(request):
    if request.method=='POST':
        image = request.POST.get('profile_byte_code')
        header , encoded =image.split(',',1)
        data = b64decode(encoded)
        with open("media/image.jpg", "wb") as f:
            f.write(data)

        fe = feature_extractor.FeatureExtractor()
        features = []
        img_paths = []

        # Append every generated PKL file into an array and the image version as well
        for feature_path in Path("./media/feature").glob("*.npy"):
            features.append(np.load(feature_path))
            img_paths.append(Path("./media/profile_pic") / (feature_path.stem + ".jpg"))
        features = np.array(features)
        # Define the query image, in our case it will be a hamburguer
        img = Image.open(Path("./media/image.jpg"))  # PIL image

        # Search for matches
        query = fe.extract(img)
        dists = np.linalg.norm(features - query, axis=1)  # Do search
        ids = np.argsort(dists)[:30] # Top 30 results
        scores = [(dists[id], img_paths[id]) for id in ids]

        # Store results in a dictionary
        results = [scores]

        
           

        # Create a JSON file with the results
        return render(request,'output.html',context={'results':results})
    return render(request,'verifydata.html')

