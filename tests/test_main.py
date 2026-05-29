**Pytest (Python)**
```python
import pytest

class LoginSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        self.users[username] = password

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

def test_login_system():
    login_system = LoginSystem()
    login_system.register('user1', 'password1')
    assert login_system.login('user1', 'password1') == True
    assert login_system.login('user1', 'wrong_password') == False
    assert login_system.login('non_existent_user', 'password') == False

def test_register():
    login_system = LoginSystem()
    login_system.register('user1', 'password1')
    assert 'user1' in login_system.users
    assert login_system.users['user1'] == 'password1'

def test_empty_system():
    login_system = LoginSystem()
    assert login_system.login('user1', 'password1') == False
    assert login_system.users == {}
```

**Jest (JavaScript)**
```javascript
describe('LoginSystem', () => {
    let loginSystem;

    beforeEach(() => {
        loginSystem = new LoginSystem();
    });

    it('should login with correct credentials', () => {
        loginSystem.register('user1', 'password1');
        expect(loginSystem.login('user1', 'password1')).toBe(true);
    });

    it('should not login with incorrect password', () => {
        loginSystem.register('user1', 'password1');
        expect(loginSystem.login('user1', 'wrong_password')).toBe(false);
    });

    it('should not login with non-existent user', () => {
        expect(loginSystem.login('non_existent_user', 'password')).toBe(false);
    });

    it('should register user', () => {
        loginSystem.register('user1', 'password1');
        expect(loginSystem.users['user1']).toBe('password1');
    });

    it('should have empty users object initially', () => {
        expect(loginSystem.users).toEqual({});
    });
});

class LoginSystem {
    constructor() {
        this.users = {};
    }

    register(username, password) {
        this.users[username] = password;
    }

    login(username, password) {
        if (username in this.users && this.users[username] === password) {
            return true;
        }
        return false;
    }
}
```
