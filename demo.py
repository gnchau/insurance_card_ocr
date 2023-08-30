from load_model import load_model
from rectify import inference

"""
Example:
from rectify import inference
from load_model import load_model
input = 'example/card.jpg'
output = 'result/card.png'
model, device = load_model()
inference(input, output, trained_model, device)
"""

if __name__ == "__main__":
    """
    Demo
    """
    input1 = 'example/card1.jpg'
    input2 = 'example/card2.jpg'
    output1 = 'result/card1.png'
    output2 = 'result/card2.png'

    trained_model, device = load_model()
    inference(input1, output1, trained_model, device)
    inference(input2, output2, trained_model, device)

    print("Done.")
