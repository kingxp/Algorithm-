import tensorflow as tf

def FSGM_tensorflow(sess,x,y,feed_dict,norm='inifinite')
	gradient = sess.run(tf.gradients(y,x)[0],feed_dict=feed_dict)
	if(norm == 'inifinite'):
		A = tf.sign(gradient)
		perb = sess.run(A,feed_dict=feed_dict)
	elif (norm=='one'):
		A = tf.norm(gradient,ord=1)
		perb = sess.run(A,feed_dict=feed_dict)
		perb*=gradient
	elif (norm=='two'):
		A = tf.norm(gradient,ord=2)
		perb = sess.run(A,feed_dict=feed_dict)
		perb*=gradient
	else:
		raise NameError("norm error")
	return perb