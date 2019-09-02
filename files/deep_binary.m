function [accuracy]= deep_binary(filename1,fielname2)
train2 = csvread(filename1);
test2 = csvread9(filename2);
for i = 1:6
[mi,k]=min(test2(:,i));
[ma,k]=max(test2(:,i));
test2(:,i) = (test2(:,i)-mi)/(ma-mi);
end
for i = 1:6
[mi,k]=min(train2(:,i));
[ma,k]=max(train2(:,i));
train2(:,i) = (train2(:,i)-mi)/(ma-mi);
end
train2(:,7) = train2(:,7)-1;
test2(:,7) = test2(:,7)-1;
x_train = train2(:,1:6);
y_train = train2(:,7);
x_test = test2(:,1:6);
y_test = test2(:,7);
rand('state',0)
dbn.sizes = [20 10 5];

opts.numepochs =   1;
opts.batchsize = 2;
opts.momentum  =   0.5;
opts.alpha     =   0.3;
dbn = dbnsetup(dbn,x_train, opts);
dbn = dbntrain(dbn,x_train, opts);
nn = dbnunfoldtonn(dbn,1);
nn.activation_function              = 'sigm';
nn.learningRate                     = 0.3;
opts2.numepochs =   100;
opts2.batchsize = 5;
nn = nntrain(nn, x_train, y_train, opts2);
nn = nnff(nn, x_test, zeros(size(x_test,1), nn.size(end)));
nn.testing = 0;
preds = nn.a{end};
for i = 1:size(preds,1)
    if (preds(i,1)>0.5)
        preds(i,1) = 1;
    else
        preds(i,1) = 0;
    end
end
err = abs(preds(:,1)-y_test(:,1));
accuracy = 1-sum(err)/200;
disp(accuracy);
end