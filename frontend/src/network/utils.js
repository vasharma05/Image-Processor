const checkAPIfailure = res => {
    res = res.hasOwnProperty('response') ? res.response : res;
    console.log(`-----------------------------${JSON.stringify(res.data)}`);
    return res.data;
  }

  export default checkAPIfailure