import base64
import os


def decode_base64(data: str) -> bytes:
    """
    base64로 인코딩된 메시지 부분을 디코딩합니다.
    인자:
        data (str): base64로 인코딩된 문자열.
    반환값:
        bytes: 디코드 결과 바이트 스트림.
    """
    data = data.replace("-", "+").replace("_", "/")
    return base64.b64decode(data)


def save_file(file_data: str, file_name: str = "attachment", save_dir: str = "downloaded_files") -> None:
    """
    파일 데이터를 정해진 경로에 저장합니다.

    Args:
        file_data (str): 문자열로 인코딩된 파일 정보
        file_path (str): 파일을 저장할 경로
    """
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, "wb") as file:
        file.write(file_data)
