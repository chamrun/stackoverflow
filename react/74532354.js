onSwiper= {(swiper)
=>
{
  setTimeout(() => {
    swiper.params.navigation.prevEl = navigationPrevRef.current;
    swiper.params.navigation.nextEl = navigationNextRef.current;
    swiper.navigation.destroy();
    swiper.navigation.init();
    swiper.navigation.update();
  });
}
}

//Unhandled Runtime Error TypeError: Cannot read properties of undefined (reading 'navigation')

//This error means that `swiper` or `swiper.params` is undefined and `navigation` cannot be read from it.
//You can check it by adding a console.log(swiper) and console.log(swiper.params) before the setTimeout.

