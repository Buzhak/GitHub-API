import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()


token = os.getenv('git_token')
user_name = os.getenv('user_name')
base_url = 'https://api.github.com'
test_repo_name = 'my_test_repo'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}


def get_all_repos() -> list[str]:
    '''
    Функция получает все репозитории пользователя на Github
    и возвращает список с названиями репозиториев
    '''

    url = f'{base_url}/users/{user_name}/repos'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        repos = list(map(lambda repo: repo['name'], repos))
        return repos
    else:
        print(f'Failed to fetch data: {response.status_code}, {response.text}')


def is_repo_exists(repo_name: str) -> None:
    '''
    Функция принимает название репозитория в виде строки
    и проверяет его наличие в общем списке репозиториев пользователя

    repo_name: str
    '''
    all_repos = get_all_repos()

    if repo_name in all_repos:
        print(f'Repository "{repo_name}" exists.')
    else:
        print(f'Repository "{repo_name}" does not exist.')


def create_new_repo(repo_name: str) -> None:
    '''
    Функция принимает название репозитория в виде строки
    и создаёт репозиторий на Github

    repo_name: str
    '''

    url = f'{base_url}/user/repos'
    data = {
        'name': repo_name,
        'description': 'Test repo',
        'private': False,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print(f'Repository "{repo_name}" created successfully!')
    else:
        print(
            f'Failed to create repository: {response.status_code}, '
            f'{response.text}'
        )


def delete_repo_by_name(repo_name: str) -> None:

    '''
    Функция принимает название репозитория в виде строки
    и удаляет репозиторий на Github

    repo_name: str
    '''

    url = f'{base_url}/repos/{user_name}/{repo_name}'
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f'Repository "{repo_name}" deleted successfully!')
    else:
        print(
            f'Failed to delete repository: {response.status_code}, '
            f'{response.text}'
        )


if __name__ == '__main__':
    create_new_repo(test_repo_name)
    is_repo_exists(test_repo_name)
    delete_repo_by_name(test_repo_name)
    is_repo_exists(test_repo_name)
