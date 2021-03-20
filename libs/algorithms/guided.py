import cv2
import numpy
import imageio


def box(img, r):            # BOX FILTER, img >=2d img, r: radius of box filter

    (rows, cols) = img.shape[:2]
    imDst = numpy.zeros_like(img)

    ## NOTA:
    # The [:, :] stands for everything from the beginning to the end just like for lists. 
    # The difference is that the first : stands for first and the second : for the second dimension.

    tile = [1] * img.ndim
    tile[0] = r
    imCum = numpy.cumsum(img, 0)
    imDst[0:r+1, :, ...] = imCum[r:2*r+1, :, ...]
    imDst[r+1:rows-r, :, ...] = imCum[2*r+1:rows, :, ...] - imCum[0:rows-2*r-1, :, ...]
    imDst[rows-r:rows, :, ...] = numpy.tile(imCum[rows-1:rows, :, ...], tile) - imCum[rows-2*r-1:rows-r-1, :, ...]

    tile = [1] * img.ndim
    tile[1] = r
    imCum = numpy.cumsum(imDst, 1)
    imDst[:, 0:r+1, ...] = imCum[:, r:2*r+1, ...]
    imDst[:, r+1:cols-r, ...] = imCum[:, 2*r+1 : cols, ...] - imCum[:, 0 : cols-2*r-1, ...]
    imDst[:, cols-r: cols, ...] = numpy.tile(imCum[:, cols-1:cols, ...], tile) - imCum[:, cols-2*r-1 : cols-r-1, ...]

    # print("******\n\n", imDst, "******")

    return imDst


def guided_filter_blackandwhite(I, p, r, eps):  # I = guide image, p: filter input, r: windows radius, eps: regularization

    Isub = I
    Psub = p

    (rows, cols) = Isub.shape # return a tuple with each index having the number of corresponding elements.

    print("AAA", rows, cols)

    N = box(numpy.ones([rows, cols]), r)

    meanI = box(Isub, r) / N
    meanP = box(Psub, r) / N
    corrI = box(Isub * Isub, r) / N
    corrIp = box(Isub * Psub, r) / N
    varI = corrI - meanI * meanI
    covIp = corrIp - meanI * meanP

    a = covIp / (varI + eps)
    b = meanP - a * meanI

    meanA = box(a, r) / N
    meanB = box(b, r) / N

    q = meanA * I + meanB
    return q


def guided_filter_color(I, p, r, eps):      # I guide image, p filtering input, r windows radius, eps regularization

    fullI = I
    fullP = p

    h, w = p.shape[:2]
    N = box(numpy.ones((h, w)), r)

    mI_r = box(I[:,:,0], r) / N
    mI_g = box(I[:,:,1], r) / N
    mI_b = box(I[:,:,2], r) / N

    mP = box(p, r) / N

    # calcolo la media di I * p
    mIp_r = box(I[:,:,0]*p, r) / N
    mIp_g = box(I[:,:,1]*p, r) / N
    mIp_b = box(I[:,:,2]*p, r) / N

    # per-patch covarianza di (I, p)
    covIp_r = mIp_r - mI_r * mP
    covIp_g = mIp_g - mI_g * mP
    covIp_b = mIp_b - mI_b * mP

    # calcolo covarianza simmetrica della matrice di I in ogni patch:
    #       rr rg rb
    #       rg gg gb
    #       rb gb bb
    var_I_rr = box(I[:,:,0] * I[:,:,0], r) / N - mI_r * mI_r;
    var_I_rg = box(I[:,:,0] * I[:,:,1], r) / N - mI_r * mI_g;
    var_I_rb = box(I[:,:,0] * I[:,:,2], r) / N - mI_r * mI_b;

    var_I_gg = box(I[:,:,1] * I[:,:,1], r) / N - mI_g * mI_g;
    var_I_gb = box(I[:,:,1] * I[:,:,2], r) / N - mI_g * mI_b;

    var_I_bb = box(I[:,:,2] * I[:,:,2], r) / N - mI_b * mI_b;

    a = numpy.zeros((h, w, 3))
    for i in range(h):
        for j in range(w):
            sig = numpy.array([
                [var_I_rr[i,j], var_I_rg[i,j], var_I_rb[i,j]],
                [var_I_rg[i,j], var_I_gg[i,j], var_I_gb[i,j]],
                [var_I_rb[i,j], var_I_gb[i,j], var_I_bb[i,j]]
            ])
            covIp = numpy.array([covIp_r[i,j], covIp_g[i,j], covIp_b[i,j]])
            a[i,j,:] = numpy.linalg.solve(sig + eps * numpy.eye(3), covIp)

    b = mP - a[:,:,0] * mI_r - a[:,:,1] * mI_g - a[:,:,2] * mI_b

    meanA = box(a, r) / N[...,numpy.newaxis]
    meanB = box(b, r) / N

    q = numpy.sum(meanA * fullI, axis=2) + meanB

    return q



# def guided_filter(I, p, r, eps):    ### I input image , guidance image g, radius r, regularization eps
                                    ## per semplicità ho rimosso p dall'input in quanto viene utilizzata come immagine guida l'immagine stessa.
def guided_filter(path, r, eps):
    """
        Args:
            path    (str)    path of input image
            r       (int)    radius
            eps     (str)    regularization 

        Returns:
            result       (ndarray) output filtered image
    """

    ## read image with imageio and divide by the interval   (if use opencv2 the result would be of different colors)
    I = imageio.imread(path).astype(numpy.float32)/255.0
    print(I.shape)

    if (I.shape[2] == 3):   ## color
        ## stack: Join a sequence of arrays along a new axis.
        I_smoothed = numpy.zeros_like(I)  # smoothed array

        for i in range(3):
            I_smoothed[:,:,i] = guided_filter_color(I, I[:,:,i], r, eps)
        return I_smoothed
    elif (I.shape[2] == 1): ### bw   ma attenzione che non funziona!!!
        return guided_filter_blackandwhite( I[:,:], I[:,:], r, eps )
    else:
        return False

def main():

    input_img = "../../static/images/cat.bmp"

    res = guided_filter(input_img, 8, 0.16)
    imageio.imwrite('../../static/images/edited/res.png', res) 

main()