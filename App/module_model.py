#module_model.py
import tensorflow as tf
import keras
new_model = tf.keras.models.load_model(r'D:\Project\HandGesture_Community_Edition\models\my_model.keras')
# show model architecture
new_model.summary()