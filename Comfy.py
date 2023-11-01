import random
import requests
import os
from dotenv import load_dotenv

load_dotenv()

comfyUrl =  os.getenv('COMFY_UI_URL') 


def gneratePhoto(userprompt, chat_id, file_number ,outputPath):

    seed = random.randint(0, 1000000)
    prompt = userprompt
    times = 0
    fileprefix = chat_id

    data = {
        "3": {
            "inputs": {
                "seed": f"{seed}",
                "steps": 20,
                "cfg": 8,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1,
                "model": [
                    "4",
                    0
                ],
                "positive": [
                    "6",
                    0
                ],
                "negative": [
                    "7",
                    0
                ],
                "latent_image": [
                    "5",
                    0
                ]
            },
            "class_type": "KSampler"
        },
        "4": {
            "inputs": {
                "ckpt_name": "sd_xl_base_1.0_0.9vae.safetensors"
            },
            "class_type": "CheckpointLoaderSimple"
        },
        "5": {
            "inputs": {
                "width": 1024,
                "height": 1024,
                "batch_size": 1
            },
            "class_type": "EmptyLatentImage"
        },
        "6": {
            "inputs": {
                "text": f"{prompt}",
                "clip": [
                    "4",
                    1
                ]
            },
            "class_type": "CLIPTextEncode"
        },
        "7": {
            "inputs": {
                "text": "",
                "clip": [
                    "4",
                    1
                ]
            },
            "class_type": "CLIPTextEncode"
        },
        "8": {
            "inputs": {
                "samples": [
                    "3",
                    0
                ],
                "vae": [
                    "4",
                    2
                ]
            },
            "class_type": "VAEDecode"
        },
        "9": {
            "inputs": {
                "filename_prefix": f"{fileprefix}",
                "images": [
                    "8",
                    0
                ]
            },
            "class_type": "SaveImage"
        },
        "11": {
            "inputs": {
                "filename_prefix": f"{chat_id}",
                "filename_keys": "",
                "foldername_prefix": f"{chat_id}",
                "foldername_keys": "",
                "delimiter": "dot",
                "save_job_data": "disabled",
                "job_data_per_image": "disabled",
                "job_custom_text": "",
                "save_metadata": "disabled",
                "counter_digits": 2,
                "counter_position": "last",
                "image_preview": "enabled",
                "images": [
                    "8",
                    0
                ]
            },
            "class_type": "SaveImageExtended"
        }

    }


    response = requests.post(comfyUrl, json={'prompt': data})
    result = response.json()


    filename = "{}.{:02d}.png".format(chat_id, int(file_number))
    imagePath = f"{outputPath}\\{chat_id}\\{filename}"
    file_number = int(file_number)
    file_number = file_number + 1
    file_number = str(file_number)

    if os.path.isdir(f'{outputPath}\\{chat_id}'):
        with open(f'{outputPath}\\{chat_id}\\{chat_id}.txt', 'w') as f:
            f.write(file_number)
    else:
        os.mkdir(f'{outputPath}\\{chat_id}')
        with open(f'{outputPath}\\{chat_id}\\{chat_id}.txt', 'w') as f:
            f.write(file_number)

    return imagePath
