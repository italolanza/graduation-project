## Numpy

+ `np.array([]]` -> creates a numpy array from a list;
+ `np.arange(start, stop, step_size)` -> Similar to Python `range` function, but creates a Numpy array;
+ `np.zeros((row, collumns)) || np.zeros(size)` -> Creates a n-size array of zeros;
+ `np.ones((row, collumns)) || np.ones(size)` -> Creates a n-size array of one's;
+ `np.linspace(start, end, num_points)` -> Cretes a array with evenly spaced numbers;
+ `np.random.randint(low_num, high_num,(row, collumn))` -> Generates a array of random integers;
+ `np.random.seed()` -> Set a seed for the random generator algorithm;
+ `np.max()` -> Return the max value of an array;
+ `np.argmax()` -> Return the index of the max value of an array;
+ `np.min()` -> Return the min value of an array;
+ `np.mean()` -> Return the mean value of an array;
+ `arr.reshape(2,5)` -> Reshapes an array;
+ `arr[row,collum]` -> It going to return the value in the specified location of the array;
  + `arr[:,0]` -> You algo use slicing.
+ `arr[arr>50]` -> Its going to return a 1-d array with all values greater than 50.

<br>

## Pandas

+ `pd.read_csv('path/to/file')` -> Creates a dataframe from a csv;
+ `pd.DataFrama(data=<np.array>)` -> Creates a dataframe from a numpy array;
+ `df['Collumn'] || df[['Collumn1, Collum2']]` -> Retrieves the selected collumn(s) from the dataframe;
+ `df['Collumn'].max()` -> Returns the max value of a collumn;
+ `df['Collumn'].describe()` -> Returns a numbers of data statitics of a collumn;

<br>

## Matplotlib and Pandas built in

### Matplotlib
+ `import matplotlib.pyplot as plt`
  + `%matplotlib inline` -> Jupyter notebook command show the plots without `plt.show()`;
  + `plt.plot(x,y,'<marker>||color')` -> Creates a simple plot;
    + `plt.xlim(start, end)`
    + `plt.ylim(start, end)` -> Set a start and end value to your plot's axis;
    + `plt.title('Title')` -> Puts a title on the plot;
    + `plt.xlabel('X LABEL')` -> Puts a label to your x axis;
    + `plt.ylabel('Y LABEL')` -> Puts a label to your y axis;
  + `plt.imshow(array)` -> Creates a plot where each value is mapped to an specific color. From brigher to darker (lower to higher value) color;
    + `plt.colorbar()` -> If you want a color bar on the side of the cart;

### Pandas Built in
+ `df.plot(x='Collumn1', y='Collumn2', kind='<type_of_chart>')`

<br>

## Scikit Learn

+ `from sklearn.pre_processing import MinMaxScaler`
  + `scaler_model = MinMaxScaler()` -> Creates your MinMaxScaler object;
    + `scaler_model.fit(data)` -> Makes the MinMaxScaler store information about your data;
    + `scaler_model.transform(data)` -> Scale your data. Divide each collumn by its maximum value;
    + `scaler.model.fit_transform(data)` -> Same as the previous two, but in one command;
+ `from sklearn.model_selection import train_test_split`
  + `X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.3), random_state=101` -> Splits your for training and test. It works on either numpy arrays or pandas dataframes;

<br>

## TensorFlow

+ `tf.constant([value])` -> Creates a 1-dimension Tensor;
+ `tf.fill((r,s),value)` -> Creates a Tensor of rank *r* (num of rows) and shape *s* (size of each row/dimension) filled with the selected value;
+ `tf.zeros((r,s))` -> Creates a Tensor of rank *r* (num of rows) and shape *s* (size of each row/dimension) filled with zeros;
+ `tf.ones((r,s))` -> Creates a Tensor of rank *r* (num of rows)  and shape *s* (size of each row/dimension) filled with ones;
+ `tf.random_normal((d,s), mean=<value>, stddev=<value>)` -> Creates a Tensor of *s* dimentions and shape *s* filled with values of a normal distribution;
+ `tf.random_uniform((d,s), minval=<value>, maxval=<value>)` -> Creates a Tensor of *s* dimentions and shape *s* filled with values of a uniform distribution;
+ `tf.Session()` -> Creates a *session* object. The session object execute operations on nodes:
  + ```python
      with tf.Session() as sess: 
        result = sess.run(node)
    ```
+ `tf.InteractiveSession()` -> Only usefull on Python notebooks. Allow us to use `sess.run(node)` with out the `with` statement;
+ `tf.matmul(tensor1, tensor2)` -> Multiply two Tensors/Matrix;
+ `tf.Graph()` -> Creates an empty *Graph* object;
+ `tf.get_default_graph()` -> Retunrs the default Graph object;
+ `with tf.Graph().as_default():`-> Runs some code using another *Graph* object as default;
+ `tf.Variable(initial_value=<Tensor>)` -> Creates a *Variable* object; 
+ `tf.global_variables_initializar()` -> Returns the initializer. After running it on a session will initialize all *Variables* objects;
+ `tf.placdeholder(dtype, shape=())` -> Creates a *Placeholder* object;