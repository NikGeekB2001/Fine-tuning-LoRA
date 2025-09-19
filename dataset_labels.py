import os
from dotenv import load_dotenv
from datasets import load_dataset

# Загрузка переменных окружения
load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

def analyze_dataset_labels():
    """Анализ меток в датасете Rexhaif/ru-med-ner"""
    print("🔍 Анализ меток в датасете Rexhaif/ru-med-ner")
    print("=" * 50)

    try:
        # Загружаем датасет
        dataset = load_dataset("Rexhaif/ru-med-ner", token=HF_API_TOKEN)
        train_dataset = dataset["train"]

        # Собираем все уникальные метки
        all_labels = set()
        for example in train_dataset:
            all_labels.update(example["ner_tags"])

        unique_labels = sorted(list(all_labels))
        print(f"📋 Найденные уникальные метки: {unique_labels}")
        print(f"Количество меток: {len(unique_labels)}")

        # Проверяем, есть ли feature names
        if hasattr(train_dataset.features["ner_tags"], 'feature') and hasattr(train_dataset.features["ner_tags"].feature, 'names'):
            feature_names = train_dataset.features["ner_tags"].feature.names
            print(f"📋 Имена меток из features: {feature_names}")
        else:
            print("❌ Имена меток не найдены в features")

        # Сравниваем с ожидаемыми метками
        expected_labels = list(range(13))  # 0 to 12
        if unique_labels == expected_labels:
            print("✅ Метки совпадают с ожидаемыми (0-12)")
        else:
            print("❌ Метки не совпадают!")
            print(f"Ожидалось: {expected_labels}")
            print(f"Получено: {unique_labels}")

    except Exception as e:
        print(f"❌ Ошибка при загрузке датасета: {e}")

def print_label_comments():
    """Комментарии к меткам на русском языке"""
    print("\n📝 Комментарии к меткам:")
    print("=" * 50)

    label_comments = {
        "0": "O - Вне сущности (Outside). Токен не относится к медицинской сущности.",
        "1": "B-DISEASE - Начало болезни (Beginning of Disease). Первый токен в названии заболевания или диагноза.",
        "2": "I-DISEASE - Продолжение болезни (Inside Disease). Последующие токены в названии заболевания или диагноза.",
        "3": "B-SYMPTOM - Начало симптома (Beginning of Symptom). Первый токен в названии симптома или жалобы пациента.",
        "4": "I-SYMPTOM - Продолжение симптома (Inside Symptom). Последующие токены в названии симптома или жалобы пациента.",
        "5": "B-DRUG - Начало лекарства (Beginning of Drug). Первый токен в названии лекарственного препарата или медикамента.",
        "6": "I-DRUG - Продолжение лекарства (Inside Drug). Последующие токены в названии лекарственного препарата или медикамента.",
        "7": "B-ANATOMY - Начало анатомии (Beginning of Anatomy). Первый токен в названии органа, ткани или части тела.",
        "8": "I-ANATOMY - Продолжение анатомии (Inside Anatomy). Последующие токены в названии органа, ткани или части тела.",
        "9": "B-PROCEDURE - Начало процедуры (Beginning of Procedure). Первый токен в названии медицинской процедуры или исследования.",
        "10": "I-PROCEDURE - Продолжение процедуры (Inside Procedure). Последующие токены в названии медицинской процедуры или исследования.",
        "11": "B-FINDING - Начало результата (Beginning of Finding). Первый токен в названии результата обследования или медицинского наблюдения.",
        "12": "I-FINDING - Продолжение результата (Inside Finding). Последующие токены в названии результата обследования или медицинского наблюдения."
    }

    for key, comment in label_comments.items():
        print(f"{key}: {comment}")

if __name__ == "__main__":
    analyze_dataset_labels()
    print_label_comments()
