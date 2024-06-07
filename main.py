from deepface import DeepFace
import json

def face_analyze(img_path: str) -> None | Exception:
    try:
        result_dict = DeepFace.analyze(img_path=img_path, actions=('age', 'gender', 'race', 'emotion'))
        with open("face_analyze.json", "w") as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        print(f'[+] Age: {result_dict[0].get("age")}')
        print(f'[+] Gender: {result_dict[0].get("gender")}')
        print(f'[+] Race:')

        for k, v in result_dict[0].get('race').items():
            print(f'{k} - {round(v, 2)}%')

        print(f'[+] Emotion:')
        for k, v in result_dict[0].get('emotion').items():
            print(f'{k} - {round(v, 2)}%')

    except Exception as _ex:
        return _ex

def main():
    face_analyze(img_path='')

if __name__ == '__main__':
    main()