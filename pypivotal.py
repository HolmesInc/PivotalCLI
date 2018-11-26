import url_runner as http
from datetime import datetime, timedelta

'''
Constructor arguments:
    token: String. API token for v5 API. https://www.pivotaltracker.com/help/api#top
'''


class PivotalIntegration:
    def __init__(self, token):
        if not token:
            raise Exception('No API token received or bad value')
        self.token = token
        self.base_url = 'https://www.pivotaltracker.com/services/v5/'
        self.projects = self.get_projects()

    def get_story(self, story_id, project_id):
        url = f'{self.base_url}projects/{project_id}/stories/{story_id}'
        story = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return story

    def get_stories(self, project_id, state=None, updated_after=None):
        if state is not None:
            url = f'{self.base_url}projects/{project_id}/stories/?with_state={state}'
        else:
            url = f'{self.base_url}projects/{project_id}/stories/'

        if updated_after is not None:
            url = f'{url}&updated_after={updated_after}'

        stories = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return stories

    def get_project(self, project_id):
        url = self.base_url + 'projects/' + project_id
        project = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return project

    def get_projects(self):
        url = self.base_url + 'projects/'
        projects = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return projects

    def get_iterations(self, project_id, limit=10, offset=0):
        url = self.base_url + 'projects/' + project_id + '/iterations'
        iterations = http.get(url, query_data={'limit': limit, 'offset': offset},
                              headers={'X-TrackerToken': self.token}, return_json=True)
        return iterations

    def get_project_memberships(self, project_id):
        url = self.base_url + 'projects/' + project_id + '/memberships'
        memberships = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return memberships

    def get_accounts(self):
        url = self.base_url + 'accounts'
        accounts = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return accounts

    def get_project_labels(self, project_id):
        url = self.base_url + 'projects/' + project_id + '/labels'
        labels = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return labels

    def get_story_owners(self, story_id, project_id):
        url = self.base_url + 'projects/' + project_id + '/stories/' + story_id + '/owners'
        owners = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return owners

    def get_story_tasks(self, story_id, project_id):
        url = self.base_url + 'projects/' + project_id + '/stories/' + story_id + '/tasks'
        tasks = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return tasks

    def get_story_comments(self, story_id, project_id):
        url = self.base_url + 'projects/' + project_id + '/stories/' + story_id + '/comments'
        comments = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return comments

    def get_story_comment(self, story_id, project_id, comment_id):
        url = self.base_url + 'projects/' + project_id + '/stories/' + story_id + '/comments/' + comment_id
        comment = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return comment

    def get_story_task(self, story_id, project_id, task_id):
        url = self.base_url + 'projects/' + project_id + '/stories/' + story_id + '/tasks/' + task_id
        task = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return task

    def get_project_epics(self, project_id):
        url = self.base_url + 'projects/' + project_id + '/epics'
        epics = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return epics

    def get_project_epic_comments(self, project_id, epic_id):
        url = self.base_url + 'projects/' + project_id + '/epics/' + epic_id + '/comments'
        epic_comments = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return epic_comments

    def get_project_epic_comments(self, project_id, epic_id, comment_id):
        url = self.base_url + 'projects/' + project_id + '/epics/' + epic_id + '/comments/' + comment_id
        epic_comment = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return epic_comment

    def get_project_epic(self, project_id, epic_id):
        url = self.base_url + 'projects/' + project_id + '/epics/' + epic_id
        epic = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return epic

    def get_epic(self, epic_id):
        url = self.base_url + '/epics/' + epic_id
        epic = http.get(url, headers={'X-TrackerToken': self.token}, return_json=True)
        return epic


class Helpers:
    def __init__(self):
        self.story_states = {
            'unstarted': 'unstarted',
            'started': 'started',
            'finished': 'finished',
            'delivered': 'delivered',
            'accepted': 'accepted',
            'rejected': 'rejected',
            'planned': 'planned',
            'unscheduled': 'unscheduled'
        }

    def two_days_before(self):
        date = datetime.now() - timedelta(days=2)
        return date.isoformat()

    def datetime_string_converter(self, iso_string):
        return datetime.strptime(iso_string, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
