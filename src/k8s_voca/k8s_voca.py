"""k8s_voca 모듈.

Please put in a description of the module.

Example:
    ``k8s_voca`` 사용법은 아래와 같습니다.

        $ pip install ./
        $ k8s_voca-ping

추가적인 설명은 여기에!

Attributes:
    nnn (int): ``사용되지 않는`` 시범용 변수

Todo:
    * 무한한 모듈의 발전 ``꿈``꾸며!
    * ``Dreaming`` of infinite module development!

"""
import sys

nnn = 1


def ping():
    """Example function with PEP 484 type annotations.

    Returns:
        리턴 없이 화면 print

    """
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(f"{'p' * n}ong")
    else:
        print('pong')


if __name__ == "__main__":
    ping()
