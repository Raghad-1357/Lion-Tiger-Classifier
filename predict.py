from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# إيقاف التدوين العلمي لسهولة القراءة
np.set_printoptions(suppress=True)

# تحميل النموذج
model = load_model("/keras_model.h5", compile=False)

# تحميل أسماء الفئات
class_names = open("/labels.txt", "r").readlines()

# إنشاء مصفوفة بيانات بالشكل المطلوب للنموذج
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# وضع مسار الصورة
image = Image.open("/test_image.jpg").convert("RGB")

# تغيير حجم الصورة إلى 224x224
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# تحويل الصورة إلى مصفوفة NumPy
image_array = np.asarray(image)

# تطبيع الصورة إلى قيم بين -1 و 1
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# إدخال الصورة إلى المصفوفة
data[0] = normalized_image_array

# التنبؤ باستخدام النموذج
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index].strip()
confidence_score = prediction[0][index]

# طباعة النتيجة
print("Class:", class_name)
print("Confidence Score:", confidence_score)