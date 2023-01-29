import http from 'k6/http';
import { urls_list } from './urls_list.js';
import { check, group, sleep, fail } from 'k6';


export let options = {
  iterations: 1,
  duration: '120m'
};

const BASE_URL = `https://${__ENV.BASEURL}`;

export default () => {

  let authHeaders = {
    headers: {
      Authorization: `Token ${__ENV.TOKEN}`,
    },
  };

  
  for(let i=0;i<urls_list.length;i++){
    let start = new Date().getTime()
    let res = http.get(`${BASE_URL}/api/v2/${urls_list[i]}`, authHeaders)
    let end = new Date().getTime()
    if(res.status === 200) {
      console.log('[✔️]  ' + res.status, '- Success', ` ${(((end-start)/1000).toFixed(2)).toString()}s   ${__ENV.METHOD}   => ${urls_list[i]}`)
    }else if(res.status === 403) {
      console.error('[❌]  ' + res.status, '- You donot have permission  ', ` ${(((end-start)/1000).toFixed(2)).toString()}s   ${__ENV.METHOD}   => ${urls_list[i]}`)
    }
    else if(res.status === 408) {
      console.error('[❌]  ' + res.status, '-  (HTTP) 408 Request Timeout  ', ` ${(((end-start)/1000).toFixed(2)).toString()}s   ${__ENV.METHOD}   => ${urls_list[i]}`)
    }
    else if(res.status === 500) {
      console.error('[❌]  ' + res.status, '-  Server Timeout  ', ` ${(((end-start)/1000).toFixed(2)).toString()}s   ${__ENV.METHOD}   => ${urls_list[i]}`)
    }
    else{
      console.error('[❌]  ' + res.status, '- Error  ', ` ${(((end-start)/1000).toFixed(2)).toString()}s   ${__ENV.METHOD}   => ${urls_list[i]}`)
    }
    check(res, { // use response here
      'Response': (r)=> r.status === 200
    });
  };
    
  sleep(1);

};
