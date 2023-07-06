"""k8s_voca 모듈.

K8s Voca Search and Output

Example:
    ``k8s_voca`` 사용법은 아래와 같습니다.

        $ pip install ./
        $ kv container
"""
import sys

K8sVoca = {
    "Container": "컨테이너는 소프트웨어 서비스를 실행하는 데 필요한 특정 버전의 프로그래밍 언어 런타임 및 라이브러리와 같은 종속 항목과 애플리케이션 코드를 함께 포함하는 경량 패키지입니다.",

    "Pod": "쿠버네티스에서 생성하고 관리할 수 있는 배포 가능한 가장 작은 컴퓨팅 단위이다.(하나이상의 컨테이너 그룹)",
    "pods": "쿠버네티스에서 생성하고 관리할 수 있는 배포 가능한 가장 작은 컴퓨팅 단위이다.(하나이상의 컨테이너 그룹)",

    "ReplicaSet": "레플리카셋의 목적은 레플리카 파드 집합의 실행을 항상 안정적으로 유지하는 것이다. 레플리카셋은 보통 명시된 동일 파드 개수에 대한 가용성을 보증하는데 사용한다.",

    "Deployment": "파드와 레플리카셋(ReplicaSet)에 대한 선언적 업데이트를 제공한다. 클러스터의 스테이트리스 애플리케이션 워크로드를 관리하기에 적합하다.",
    "deployments": "파드와 레플리카셋(ReplicaSet)에 대한 선언적 업데이트를 제공한다. 클러스터의 스테이트리스 애플리케이션 워크로드를 관리하기에 적합하다.",

    "StatefulSet": "어떻게든 스테이트(state)를 추적하는 하나 이상의 파드를 동작하게 해준다. 예를 들면, 워크로드가 데이터를 지속적으로 기록하는 경우, 사용자는 Pod 와 PersistentVolume을 연계하는 StatefulSet 을 실행할 수 있다. 전체적인 회복력 향상을 위해서, StatefulSet 의 Pods 에서 동작 중인 코드는 동일한 StatefulSet 의 다른 Pods 로 데이터를 복제할 수 있다.",
    "DaemonSet": "노드-로컬 기능(node-local facilities)을 제공하는 Pods 를 정의한다. 이러한 기능들은 클러스터를 운용하는 데 기본적인 것일 것이다. 예를 들면, 네트워킹 지원 도구 또는 add-on 등이 있다. DaemonSet 의 명세에 맞는 노드를 클러스터에 추가할 때마다, 컨트롤 플레인은 해당 신규 노드에 DaemonSet 을 위한 Pod 를 스케줄한다.",
    "Job": "단 한번만 실행 완료 후 중단되는 작업을 정의",
    "CronJob": "스케줄에 따라 반복되고 실행 완료 후 중단되는 작업을 정의",
    "Static Pod": "스태틱 파드는API 서버없이 특정 노드에 있는 kubelet 데몬에 의해 직접 관리된다. 컨트롤 플레인에 의해 관리되는 파드(예를 들어디플로이먼트(Deployment))와는 달리, kubelet 이 각각의 스태틱 파드를 감시한다. (만약 실패할 경우 다시 구동한다.)",

    "노드": "쿠버네티스는 컨테이너를 파드내에 배치하고 노드 에서 실행함으로 워크로드를 구동한다. 노드는 클러스터에 따라 가상(EC2) 또는 물리적 머신일 수 있다.",
    "node": "쿠버네티스는 컨테이너를 파드내에 배치하고 노드 에서 실행함으로 워크로드를 구동한다. 노드는 클러스터에 따라 가상(EC2) 또는 물리적 머신일 수 있다.",

    "컨트롤 플레인(마스터 노드)": "컨트롤 플레인은 워커 노드와 클러스터 내 파드를 관리한다.",
    "데이타 플레인(워커 노드)": "워커 노드는 애플리케이션의 구성요소인 파드를 호스트한다.",

    "ConfigMap": "컨피그맵은 키-값 쌍으로 기밀이 아닌 데이터를 저장",

    "Secret": "암호, 토큰 또는 키와 같은 소량의 중요한 데이터를 포함하는 오브젝트",

    "서비스": "파드 집합에서 실행중인 애플리케이션을 네트워크 서비스로 노출하는 추상화 방법",
    "services": "파드 집합에서 실행중인 애플리케이션을 네트워크 서비스로 노출하는 추상화 방법",
    "service": "파드 집합에서 실행중인 애플리케이션을 네트워크 서비스로 노출하는 추상화 방법",

    "네임스페이스": "네임스페이스 는 단일 클러스터 내에서의 리소스 그룹 격리 메커니즘을 제공한다."
}


def ping():
    """K8s Voca Search and Output
    """
    if len(sys.argv) > 1:
        query = sys.argv[1]

        for word, meaning in K8sVoca.items():
            if word.lower() == query.lower():
                print(f'>> {meaning}')
    else:
        for word, meaning in K8sVoca.items():
            print(f'{word}: {meaning}')


if __name__ == "__main__":
    ping()
