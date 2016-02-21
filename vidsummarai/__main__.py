"""
VidSummarAI is a tool that uses deep learning
to summarize a videos content. 

The majority of the code in this directory is for training
the model, exploring the relationships between ratings, and
building our data pipeline.
"""

import argparse

# TODO: Do we actually need/want a CLI?
def main():
    parser = argparse.ArgumentParser(
        description="VidSummarAI is tool to summarize videos.")

    # Just tossing this here until we actually have params we want.
    parser.add_argument('-t', '--train', dest='train',
                        action='store_true', help='Train the model')
    parser.set_defaults(train=False)
    
    args = parser.parse_args()
    
if __name__ == "__main__":
    main()
