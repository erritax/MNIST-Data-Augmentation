# MNIST Data Augmentation using Gemini 2.0

MNIST (Modified National Institute of Standards and Technology) is a large dataset of 70,000 handwritten digits (0-9). It's widely used for training image processing and classification models due to its robust size and variety. However, there are still limitations. For instance, all digits are 28 x 28 pixels and greyscale. This raises concerns about its implications due to the lack of real-world noise in the dataset.

LLMs have become increasingly robust over the years, capable of generating outputs in seconds. This program shows the basics for creating an API that takes in randomly selected images in MNIST and prompts Gemini 2.0 Flash Preview Image Generation to create an additional image, requesting geometric, elastic, and color space transformations. This simple application demonstrates the strength of utilizing LLMs to augment datasets as the retrieval of large, diverse, and high-quality datasets becomes increasingly challenging and time-consuming.

Example:



*Input:

![image](https://github.com/user-attachments/assets/b7dacd38-18be-4759-9513-e2b26d17a0de)

*Output:
![image](https://github.com/user-attachments/assets/fe3a5e0e-15ba-4713-bd52-494381c7aa2c)
