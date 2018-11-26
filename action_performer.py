import sys
import shlex
import argparse
from pypivotal import PivotalIntegration, Helpers


def import_stories(token, project_id):
    pivotal = PivotalIntegration(token)
    tools = Helpers()

    stories = pivotal.get_stories(
        project_id, tools.story_states['finished'], tools.two_days_before()
    )
    for story in stories:
        url = story['url']
        created = tools.datetime_string_converter(story['created_at'])
        print(f'Ticket URL: {url}')
        print(f'Creation date: {created}')


def get_projects(token):
    pivotal = PivotalIntegration(token)
    for project in pivotal.projects:
        print(f'Name: {project["name"]} - ID: {project["id"]}')


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'token',
        help='Your token to Pivotal Tracker -> https://www.pivotaltracker.com/profile#api'
    )
    start_args = parser.parse_args(argv)

    while True:
        print('Enter one of command: projects, stories')

        command, *args = shlex.split(input('> '))

        if command == 'exit':
            break

        elif command == 'help':
            print('Enter exit')

        elif command == 'projects':
            get_projects(start_args.token)

        elif command == 'stories':
            import_stories(start_args.token, args[0])

        else:
            print('Unknown command: {}'.format(command))


if __name__ == '__main__':
    main(sys.argv[1:])
