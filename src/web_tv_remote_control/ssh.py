import paramiko

from .config import config

def ssh_api_and_turn_off():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    client.load_host_keys(config.ssh_known_hosts)

    try:
        client.connect(
            hostname=config.ssh_host,
            port=config.ssh_port,
            username=config.ssh_user,
            key_filename=config.ssh_key,
            timeout=5,
            look_for_keys=False,
            allow_agent=False,
        )
        # the remote authorized_keys "command=" restriction forces poweroff
        # regardless of what we send here, but we send it explicitly for clarity.
        stdin, stdout, stderr = client.exec_command("poweroff", timeout=5)
        stdout.channel.settimeout(5)
        exit_status = stdout.channel.recv_exit_status()
        return exit_status == 0
    except (paramiko.SSHException, OSError) as e:
        print(f"SSH poweroff failed: {e}")
        return False
    finally:
        client.close()
