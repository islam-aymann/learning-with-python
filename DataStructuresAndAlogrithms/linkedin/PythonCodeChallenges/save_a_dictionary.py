import pickle


def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)


def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    dct = {
        "name": "Nada",
        "age": 12,
        "height": 165
    }
    save_dict(dct, 'test_dict.pickle')
    recovered = load_dict('test_dict.pickle')
    print(recovered)
