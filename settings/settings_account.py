import os

class SessionsRead:
    def __init__(self):
        self.sessions = []
        for session in os.listdir('accounts'):
            if session[-7:] == 'account':
                session = open(f'accounts/{session}', 'r')
                self.sessions.append(session.read())
