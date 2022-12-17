console.log("CSRF token:", csrf_token);

const basic_url =  window.location.protocol + '//' + window.location.host + '/'         /* 'http://localhost:8000/' */

const data = {
    "id": 100,
}

const get = (url) => {
    return new Promise((succeed, fail) => {
        const xhr = new XMLHttpRequest();

        xhr.open('GET', url);
        xhr.setRequestHeader('X-CSRFToken', csrf_token);
        xhr.send();

        xhr.addEventListener('load', () => {
            if (xhr.status >= 200 && xhr.status < 400) {
                succeed(xhr.response);
            }
            else {
                fail(new Error(`Request on url - ${url} failed: ${xhr.statusText}`));
            }
        });

        xhr.addEventListener('error', () => fail(new Error(`Network error: ${xhr.status}`)));
    });
};

const post = (url, data) => {
    return new Promise((succeed, fail) => {
        const xhr = new XMLHttpRequest();

        xhr.open('POST', url);
        xhr.setRequestHeader('X-CSRFToken', csrf_token);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify(data));

        xhr.addEventListener('load', () => {
            if (xhr.status >= 200 && xhr.status < 400) {
                succeed(xhr.response);
            }
            else {
                fail(new Error(`Request on url - ${url} failed: ${xhr.statusText}`));
            }
        });

        xhr.addEventListener('error', () => fail(new Error(`Network error: ${xhr.status}`)));
    });
};

/* get(basic_url + 'api/')
   .then(res => console.log(res))
   .catch(err => console.error(err)); */

get(basic_url + 'api/cart/')
   .then(res => console.log(JSON.parse(res)))
   .catch(err => console.error(err));

post(basic_url + 'api/cart/', data)
  .then(res => console.log(JSON.parse(res)))
  .catch(err => console.error(err));

get(basic_url + 'api/cart/')
   .then(res => console.log(JSON.parse(res)))
   .catch(err => console.error(err));