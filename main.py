from PIL import Image

image_path_list = ['resim1.jpg', 'resim2.jpg', 'resim3.jpg','resim4.jpg','resim5.jpg','resim6.jpg']

image_list = [Image.open(file) for file in image_path_list]

image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[1:],
            duration=1000,
            loop=0)