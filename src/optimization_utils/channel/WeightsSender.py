from .plot_web import plot_image
import requests
"""
Used to debug model weights
"""

def SendModel(host, model, epoch):
    for (name, parameters) in model.named_parameters():
        print(name)
        weight = parameters.detach().numpy()
        if 2 == len(weight.shape):
            #print(weight.shape)
            plot = plot_image(weight, epoch)
            requests.post(host + "/weight",json={
                "name": name,
                "plot": plot
            })


#        print(np.mean(parameters.detach().numpy(), axis=0).shape)
#    exit(0)
