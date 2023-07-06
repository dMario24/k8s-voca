import sys
import k8s_voca


def test_ping():
    sys.argv = ['foo', '10']
    k8s_voca.ping()

