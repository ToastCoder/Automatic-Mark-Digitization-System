#-------------------------------------------------------------------------------------------------------------------------------

# AUTOMATIC MARK DIGITIZATION

# GETS THE IMAGE FROM THE USER AND EXTRACTS THE RESPECTIVE ROLL.NO AND THEIR MARK AND UPDATES IT IN A .CSV FILE.

# FILE NAME: MAIN.PY

# DONE BY: VIGNESHWAR RAVICHANDAR

# TOPICS: Deep Learning, TensorFlow, Convolutional Neural Networks, Multiclass Classification

#-------------------------------------------------------------------------------------------------------------------------------

# IMPORTING REQUIRED LIBRARIES
import os
import argparse

# FUNCTION TO CONVERT STR INPUT TO BOOL
def strBool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Expected a Boolean Value.')

# FUNCTION FOR PARSING
def parse():
    parser = argparse.ArgumentParser(description = 'Command Line Interface for Automatic Mark Digitization.')

    parser.add_argument('-tr','--train', 
                        type = strBool, 
                        help = 'Argument taken for training model.', 
                        default = "False")

    parser.add_argument('-req','--install_requirements', 
                        type = strBool, 
                        help = 'Argument taken for installing requirements', 
                        default = False)

    parser.add_argument('-t','--test', 
                        type = strBool, 
                        help = 'Argument for testing with custom input',
                        required = True)

    args = parser.parse_args()
    return args

# MAIN FUNCTION
if __name__ == "__main__":

    # DISABLING TENSORFLOW DEBUGGING INFORMATION
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
    print("TensorFlow Debugging Information is hidden.")
    
    args = parse()

    if (args.install_requirements):
        os.system('sudo apt install python3-pip')
        os.system('pip3 install -r requirements.txt')

    if (args.train):
        os.system('python3 src/train.py')

    if (args.test):
        os.system('python3 src/test.py')