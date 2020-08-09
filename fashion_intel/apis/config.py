# Contains the configuration files for training and dataloader
# Edit the configuration file as per your needs

NUM_CLASSES = 24
DETECTION_THRESHOLD = 0.25

BACKBONE = "resnet_50"
MODEL_SAVE_PATH = "models/faster_rcnn_{}.pt".format(BACKBONE)

OUTPUT_PATH = "outputs/"

PREDICT_IMAGE = None
SAVE_IMAGE = None
SAVE_DIR = "outputs/"


# Configuration for feed api
scores_path = "./data/tables/scores.csv"

# Configuration for reccomender api
ids_path = "./data/tables/smol.csv"
features_dir = "./data/features"

# Configuration for tagger api
state_path = "./models/tagger.pt"
vec_dir = "./data/features"
util_dir = "./data/utils"
