import json 

def load_json_file(file_path):
  """
  주어진 경로의 JSON 파일을 불러와 파이썬 객체로 변환하여 리턴합니다.

  :param file_path: 
  """

  try:
    with open(file_path, 'r', encoding='utf-8')as file:
      data = json.load(file)
    return data

  except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")

  except json.JSONDecodeError:
    print(f"JSON 디코딩 오류가 발생했습니다: {file_path}")

  except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다.: {e}")

if __name__ == "__main__":
  file_path = 'pitcher.json'
  json_data = load_json_file(file_path)
  if json_data is not None:
    print(json_data)