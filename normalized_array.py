import numpy as np

def normalized_array(data):
    """
    מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.
    
    הנוסחה לביצוע:
    x_norm = (x - min) / (max - min)
    
    פרמטרים:
    data (list or np.array): מערך של מספרים.
    
    מחזירה:
    np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
    """
    data = np.array(data)
    if np.all(data == data[0]):
        return np.zeros(data.shape)
    return (data - np.min(data)) / (np.max(data) - np.min(data))

if __name__ == "__main__":
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
