import schedule
import time
from datetime import datetime, timedelta

def run_appointment():
    """执行预约任务"""
    print(f"开始执行预约任务: {datetime.now()}")
    # 这里放您的预约代码
    import subprocess
    subprocess.run([
        '/opt/homebrew/Caskroom/miniconda/base/bin/conda', 
        'run', 
        '-n', 
        'myenv', 
        'jupyter', 
        'nbconvert', 
        '--to', 
        'notebook', 
        '--execute', 
        '/Users/pengchengxin/Downloads/project/temp/reptile/AppointmentGui.ipynb'
    ])
    print(f"预约任务执行完成: {datetime.now()}")

def main():
    # 设置目标时间（例如：今天下午14:59）
    target_time = datetime.now().replace(hour=14, minute=59, second=10, microsecond=0)
    
    # 如果目标时间已经过了，就设置为明天
    if datetime.now() > target_time:
        target_time = target_time + timedelta(days=1)
    
    print(f"任务将在 {target_time} 执行")
    
    # 计算需要等待的秒数
    wait_seconds = (target_time - datetime.now()).total_seconds()
    
    # 等待到指定时间
    time.sleep(wait_seconds)
    
    # 执行任务
    run_appointment()

if __name__ == "__main__":
    main()