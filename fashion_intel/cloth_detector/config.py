# Contains the configuration files for training and dataloader
# Edit the configuration file as per your needs


TRAIN_CSV_PATH = "df_train2.csv"
VALIDATION_CSV_PATH = "df_val2.csv"
TARGET_COL = "final_target"
TRAIN_BATCH_SIZE = 4
VALID_BATCH_SIZE = 4
TRAIN_WORKERS = 4
LEARNING_RATE = 1e-3
EPOCHS = 3
NUM_CLASSES = 24
DETECTION_THRESHOLD = 0.25

BACKBONE = "resnet_50"
MODEL_SAVE_PATH = "faster_rcnn_{}_cloth.pt".format(BACKBONE)
# valid_batch_size = 4
# valid_workers = 2

OUTPUT_PATH = "outputs/"

PREDICT_IMAGE = None
SAVE_IMAGE = None
SAVE_DIR = "outputs/"
