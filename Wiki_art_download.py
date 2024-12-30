import kagglehub

# Download latest version
path = kagglehub.dataset_download("ipythonx/wikiart-gangogh-creating-art-gan")

print("Path to dataset files:", path)