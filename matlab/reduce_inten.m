function[image] = reduce_inten(img, lvl)

% lvl is the level of internsity of image reduction expected for the given image img

if (floor(lvl)~=lvl | lvl<=0 | lvl>255| lvl ~= pow2(nextpow2(lvl)))
    error('Invalid level')
endif

img = floor(image/lvl)*lvl;

endfunction
