import numpy as np

import random
from keras.models import Model
from keras.layers import Input, Dense, LSTM, Conv1D, Activation
from keras.optimizers import Adam

def chunk_maker(v):
    patatesler = []
    for i in range(0, (v.shape[0]) // 14 - 1):
        chunk = v[i*14:(i+1)*14]
        patatesler.append(chunk.reshape(1, 14, 1))
    return np.vstack(patatesler)

def reshaper(v):
    l = v.shape[0]
    return v.reshape(l, 1)

def subsample(l, y, n=1):
    start = random.randint(0, l.shape[0]- (n+1))
    subsample = l[start:start+n]
    suby = y[start: start+n]
    init = np.zeros((len(l) - n, 1))
    return np.concatenate([init, subsample], axis=0), np.concatenate([init, suby], axis=0)

def augment(xs, ys, times=5):
    d, ts, f = xs.shape
    aug_xs = []
    aug_ys = []
    for i in range(d):
        for j in range(times-1):
            random.seed(12)
            q = random.randint(0, ts - 1)
            ax, ay = subsample(xs[i], ys[i], n=q)
            aug_xs.append(ax.reshape(1, ts, f))
            aug_ys.append(ay.reshape(1, ts, f))
    aug_xs = np.vstack(aug_xs)
    aug_ys = np.vstack(aug_ys)
    xs = np.concatenate([xs, aug_xs], axis=0)
    ys = np.concatenate([ys, aug_ys], axis=0)
    return xs, ys

def prep_data(fname):
    days = []
    with open(fname) as f:
        for i, line in enumerate(f):
            if i:
                seq = float(line.rstrip().split(',')[-1])
                days.append(seq)

    days = np.array(days[::-1])
    days -= days.min()
    days /= days.max()

    n = days.shape[0]
    tr = days[:-int(0.2*n)]
    te = days[-int(0.2*n):]
    trd = tr[:-1]
    trl = tr[1:]
    ted = te[:-1]
    tel = te[1:]

    return chunk_maker(trd), chunk_maker(trl), chunk_maker(ted), chunk_maker(tel)

def lstm():
    inp = Input(shape=(14, 1))
    x = LSTM(32, return_sequences=True)(inp)
    x = Dense(1, activation='relu')(x)
    return Model(inputs=inp, outputs=x)

if __name__ == '__main__':
    trd, trl, ted, tel = prep_data('out.csv')

    trd, trl = augment(trd, trl, times=10)
    ted, tel = augment(ted, tel, times=10)

    np.save('trd.npy', trd)
    np.save('trl.npy', trl)
    np.save('ted.npy', ted)
    np.save('tel.npy', tel)

    epochs = 50
    lr = 1e-3
    decay = lr / epochs
    adam = Adam(lr=lr, decay=decay)

    model = lstm()

    model.summary()
    model.compile(loss='mse', optimizer=adam)
    model.fit(trd, trl, batch_size=14, epochs=epochs, validation_data=[ted, tel], shuffle=True)
    model.save_weights("model.h5")
