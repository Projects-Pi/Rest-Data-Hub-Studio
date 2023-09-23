import os
import subprocess
import click
from termcolor import colored

# Define the project structure and flow-compose mapping
PROJECT_STRUCTURE = {
    'AuthFlow': ['AdminUserFlow'],
    'DataFlow': ['GeneVariant'],
    'UtilFlow': ['PostgresFlow', 'PGAdminFlow']
}

# Define the path to the src directory
SRC_PATH = os.path.join(os.getcwd(), 'src')

# Define the paths to flow-compose files
FLOW_COMPOSE_PATHS = {
    'AdminUserFlow': os.path.join(SRC_PATH, 'AuthFlow', 'AdminUserFlow', 'docker-compose.yml'),
    #'UserFlow': os.path.join(SRC_PATH, 'AuthFlow', 'UserFlow', 'docker-compose.yml'),
    'GeneVariant': os.path.join(SRC_PATH, 'DataFlow', 'GeneVariant', 'docker-compose.yml'),
    'PostgresFlow': os.path.join(SRC_PATH, 'UtilFlow', 'PostgresFlow', 'docker-compose.yml'),
    'PGAdminFlow': os.path.join(SRC_PATH, 'UtilFlow', 'PGAdminFlow', 'docker-compose.yml')
    #'HaProxyFlow': os.path.join(SRC_PATH, 'UtilFlow', 'HaProxyFlow', 'docker-compose.yml')
}

# Helper function to validate flow name
def validate_flow(ctx, param, value):
    if value not in PROJECT_STRUCTURE:
        raise click.BadParameter(f'Invalid flow name. Available flows: {", ".join(PROJECT_STRUCTURE.keys())}')
    return value

# Define colors for each part
FLOW_COLOR = 'blue'
SERVICES_COLOR = 'yellow'
CONTAINER_COLOR = 'magenta'  # You can change this to your desired container name color

# Helper function to colorize log prefixes
def colorize_log_prefix(flow, service=None, container=None, command=None):
    flow_colored = colored(f'[{flow}]', FLOW_COLOR)
    services_colored = colored('[All Services]', SERVICES_COLOR)
    service_colored = colored(f'[{service}]', SERVICES_COLOR) if service else services_colored
    command_colored = colored(command.capitalize(), 'magenta') if command else ""
    container_colored = colored(f'[{container}]', CONTAINER_COLOR) if container else ""

    if container:
        return f'{flow_colored} {service_colored} {command_colored} {container_colored}'
    elif service:
        return f'{flow_colored} {service_colored} {command_colored}'
    else:
        return f'{flow_colored} {services_colored} {command_colored}'

# Helper function to start, build, stop, view logs, and purge services
def manage_services(flow, services, all, command, command_args=None):
    if all:
        for service_name in PROJECT_STRUCTURE[flow]:
            compose_path = FLOW_COMPOSE_PATHS[service_name]
            log_and_command_prefix = colorize_log_prefix(flow, service_name, command=command)
            click.echo(f'{log_and_command_prefix} all services for {service_name}...')
            cmd = ['docker-compose', '-f', compose_path, command]
            if command_args:
                cmd.extend(command_args)
            with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True, stdin=subprocess.PIPE) as proc:
                for line in proc.stdout:
                    click.echo(f'{log_and_command_prefix} {line}', nl=False)

    elif services:
        for service in services:
            if service not in PROJECT_STRUCTURE[flow]:
                raise click.BadParameter(f'Invalid service name for {flow}. Available services: {", ".join(PROJECT_STRUCTURE[flow])}')
            compose_path = FLOW_COMPOSE_PATHS[service]
            log_and_command_prefix = colorize_log_prefix(flow, service, command=command)
            click.echo(f'{log_and_command_prefix} {command.capitalize()} {service} for {flow}...')
            cmd = ['docker-compose', '-f', compose_path, command]
            if command_args:
                cmd.extend(command_args)
            with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True, stdin=subprocess.PIPE) as proc:
                for line in proc.stdout:
                    click.echo(f'{log_and_command_prefix} {line}', nl=False)

    else:
        compose_path = FLOW_COMPOSE_PATHS[flow]
        log_and_command_prefix = colorize_log_prefix(flow, command=command)
        click.echo(f'{log_and_command_prefix} {command.capitalize()} all services for {flow}...')
        cmd = ['docker-compose', '-f', compose_path, command]
        if command_args:
            cmd.extend(command_args)
        with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True, stdin=subprocess.PIPE) as proc:
            for line in proc.stdout:
                click.echo(f'{log_and_command_prefix} {line}', nl=False)

@click.group()
def cli():
    """
    Docker Compose management for flows in DataHub.
    """
    pass

@cli.command()
@click.argument('flow', callback=validate_flow)
@click.argument('services', required=False, nargs=-1)
@click.option('--all', is_flag=True, help='Start all services for the flow')
def up(flow, services, all):
    """
    Start Docker Compose services for a flow.
    """
    manage_services(flow, services, all, 'up', command_args=['-d'])

@cli.command()
@click.argument('flow', callback=validate_flow)
@click.argument('services', required=False, nargs=-1)
@click.option('--all', is_flag=True, help='Build all services for the flow')
def build(flow, services, all):
    """
    Build Docker Compose services for a flow.
    """
    manage_services(flow, services, all, 'build')

@cli.command()
@click.argument('flow', callback=validate_flow)
@click.argument('service', required=False)
@click.option('--all', is_flag=True, help='Stop all services for the flow')
def down(flow, service, all):
    """
    Stop Docker Compose services for a flow.
    """
    manage_services(flow, [service], all, 'down', command_args=['--remove-orphans'])

@cli.command()
@click.argument('flow', callback=validate_flow)
@click.argument('service', required=False)
@click.option('--all', is_flag=True, help='View logs for all services in the flow')
def logs(flow, service, all):
    """
    View Docker Compose logs for a flow or service.
    """
    manage_services(flow, [service], all, 'logs', command_args=['-f'])

@cli.command()
@click.argument('flow', callback=validate_flow)
@click.argument('services', required=False, nargs=-1)
@click.option('--all', is_flag=True, help='Purge all services for the flow')
def purge(flow, services, all):
    """
    Purge Docker Compose services for a flow.
    """
    manage_services(flow, services, all, 'down', command_args=['-v', '--remove-orphans'])

if __name__ == '__main__':
    cli()
