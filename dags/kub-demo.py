from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

# Define default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "retries": 1,
}

# Define the DAG
with DAG(
    dag_id="k8s_pod_operator_demo",
    default_args=default_args,
    schedule_interval=None,  # Set to None for manual triggering
    catchup=False,
) as dag:

    # Task: Run a simple echo command inside a Kubernetes pod
    k8s_task = KubernetesPodOperator(
        namespace="airflow",  # Change to your Airflow namespace
        image="alpine:latest",
        cmds=["sh", "-c", "echo 'Hello from Kubernetes Pod!'"],
        name="hello-k8s-pod",
        task_id="run_k8s_task",
        get_logs=True,  # Capture logs in Airflow UI
    )

    k8s_task  # Define the task execution

