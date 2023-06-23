import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class IATraining:
    def __init__(self, model_path, dataset_path):
        self.model_path = model_path
        self.dataset_path = dataset_path
        self.model = load_model(model_path)
        self.input_shape = self.model.layers[0].input_shape[1:3]

    def train_model(self, epochs=5, batch_size=32):
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True
        )

        train_generator = train_datagen.flow_from_directory(
            self.dataset_path,
            target_size=self.input_shape,
            batch_size=batch_size,
            class_mode='binary'
        )

        self.model.fit(
            train_generator,
            steps_per_epoch=len(train_generator),
            epochs=epochs
        )

        self.save_model()

    def save_model(self):
        self.model.save(self.model_path)

if __name__ == "__main__":
    model_path = "path/to/accident_detection_model.h5"
    dataset_path = "path/to/dataset"
    ia_training = IATraining(model_path, dataset_path)
    ia_training.train_model(epochs=5, batch_size=32)
