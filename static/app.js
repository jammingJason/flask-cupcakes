async function getCupcakes() {
  let ccHolder = document.querySelector('#ccHolder');
  await axios
    .get('/api/cupcakes')
    .then((response) => {
      let cc = response.data.cupcakes;
      //   return cc.serialize();
      //   console.log(cc);
      for (const key in cc) {
        if (Object.hasOwnProperty.call(cc, key)) {
          const element = cc[key];
          showCupcake(element);
        }
      }
    })
    .catch((error) => {
      console.log(error);
    });
}

function showCupcake(cupcake) {
  let ccHolder = document.querySelector('#ccHolder');

  let newTr = document.createElement('tr');
  let imageTd = document.createElement('td');

  let flavorTd = document.createElement('td');
  let sizeTd = document.createElement('td');
  let newImg = document.createElement('img');
  let ratingTd = document.createElement('td');
  // newImg.class = 'ccImage';
  newImg.src = cupcake.image;
  imageTd.innerHTML = `<img src=${cupcake.image}>`;
  flavorTd.innerText = cupcake.flavor;
  sizeTd.innerText = cupcake.size;
  ratingTd.innerText = cupcake.rating;
  newTr.margin = '2';
  ccHolder.append(newTr);
  newTr.append(imageTd);
  newTr.append(flavorTd);
  newTr.append(sizeTd);
  newTr.append(ratingTd);
}

getCupcakes();

async function addCupcake() {
  const flavor = document.querySelector('#ccFlavor');
  const size = document.querySelector('#ccSize');
  const rating = document.querySelector('#ccRating');
  let image = document.querySelector('#ccImage');
  if (image.value == '') {
    image.value = 'https://tinyurl.com/demo-cupcake';
  }
  await axios
    .post('api/cupcakes', {
      flavor: flavor.value,
      size: size.value,
      rating: rating.value,
      image: image.value,
    })
    .then((response) => {
      flavor.value = '';
      size.value = 'small';
      rating.value = '';
      image.value = '';
      showCupcake(response.data.cupcake);
    });
}
