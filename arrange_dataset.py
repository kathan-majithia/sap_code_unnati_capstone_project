import os
import shutil

# CHANGE THESE PATHS ACCORDING TO YOUR SYSTEM
SOURCE_TRAIN = r"E:\archive\sign_data\train"
SOURCE_TEST = r"E:\archive\sign_data\test"

DEST_TRAIN_GENUINE = "dataset/train/genuine"
DEST_TRAIN_FORGED = "dataset/train/forged"

DEST_TEST_GENUINE = "dataset/test/genuine"
DEST_TEST_FORGED = "dataset/test/forged"


def copy_images(source_dir, genuine_dest, forged_dest):
    for folder in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder)

        if not os.path.isdir(folder_path):
            continue

        # Decide class
        if folder.endswith("_forg"):
            dest = forged_dest
        else:
            dest = genuine_dest

        for img in os.listdir(folder_path):
            src_img_path = os.path.join(folder_path, img)

            if img.lower().endswith(('.png', '.jpg', '.jpeg')):
                new_name = f"{folder}_{img}"
                dest_img_path = os.path.join(dest, new_name)

                shutil.copy(src_img_path, dest_img_path)


# Process train and test
copy_images(SOURCE_TRAIN, DEST_TRAIN_GENUINE, DEST_TRAIN_FORGED)
copy_images(SOURCE_TEST, DEST_TEST_GENUINE, DEST_TEST_FORGED)

print("✅ Dataset arranged successfully!")
