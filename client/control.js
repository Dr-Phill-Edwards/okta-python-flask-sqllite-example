var accessToken = null;

var signIn = new OktaSignIn({
    baseUrl: 'http://dev-436256.okta.com',
    clientId: '0oaavsqp2YFRRTL5x5d5',
    redirectUri: window.location.origin,
    authParams: {
        issuer: 'https://dev-436256.okta.com/oauth2/default',
        responseType: ['token', 'id_token']
    }
});

signIn.renderEl({
    el: '#widget-container'
}, function success(res) {
    if (res.status === 'SUCCESS') {
        accessToken = res.tokens.accessToken.accessToken;
        signIn.hide();
        onmessage()
    } else {
        alert('fail);')
    }
}, function(error) {
    alert('error ' + error);
});

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