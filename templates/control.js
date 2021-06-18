var accessToken = null;

var signIn = new OktaSignIn({
    el: '#widget-container',
    baseUrl: '{{okta_domain}}',
});

signIn.showSignInToGetTokens({
    clientId: '{{okta_client_id}}',
    redirectUri: window.location.origin,
    scopes: ['openid', 'profile']
}).then(function(tokens) {
    accessToken = tokens.accessToken.accessToken;
    signIn.hide();
    loadmessages()
}).catch(function(error) {
    alert('error ' + error);
});

function loadmessages() {
    const url = "/api/messages";
    var headers = {}
    if (accessToken != null) {
        headers = { 'Authorization': 'Bearer ' + accessToken }
    }
    fetch(url, {
        method : "GET",
        mode: 'cors',
        headers: headers
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(response.json())
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('messages').value = data.messages.join('\n');
    })
    .catch(function(error) {
        document.getElementById('messages').value = error;
    });
}

function onmessage() {
    const url = "/api/messages";
    var headers = {}
    if (accessToken != null) {
        headers = { 'Authorization': 'Bearer ' + accessToken }
    }
    fetch(url, {
        method : "POST",
        mode: 'cors',
        headers: headers,
        body: new URLSearchParams(new FormData(document.getElementById("messageForm"))),
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(response.json())
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('messages').value = data.messages.join('\n');
    })
    .catch(function(error) {
        document.getElementById('messages').value = error;
    });
}