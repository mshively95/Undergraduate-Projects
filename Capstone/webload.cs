using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class WebLoad : MonoBehaviour 
{
	public GameObject cube;
	public GameObject cube1;
	
	string str = "cubeposition";
	string str1 = "cubeposition1";
	
	public void Start()
	{
		
		
		StartCoroutine("DownloadMesh");
		StartCoroutine("DownloadMesh1");

	}
	
	public IEnumerator DownloadMesh()
{
    // Create a URL and add parameters to the end of it.
    string myURL = "http://cgi.soic.indiana.edu/~team05/ES2.php";
    myURL += "?webfilename=" + str + "&webusername=tsajnani&webpassword=Capstone2017";
 
    // Create our ES2Web object.
    ES2Web web = new ES2Web(myURL + "&tag=tag");
      
    // Start downloading our data and wait for it to finish.
    yield return StartCoroutine(web.Download());
      
    if(web.isError)
    {
        // Enter your own code to handle errors here.
        Debug.LogError(web.errorCode + ":" + web.error);
    }
    else
    {
 
        // Or we could just load directly from the ES2Web object.
        Vector3 cubepos = web.Load<Vector3>("tag");
		Load(cubepos);
    }
	
}
	public void Load(Vector3 cubepos)
	{
		cube.transform.position = cubepos;

	}

	public IEnumerator DownloadMesh1()
{
    // Create a URL and add parameters to the end of it.
    string myURL = "http://cgi.soic.indiana.edu/~team05/ES2.php";
    myURL += "?webfilename=" + str1 + "&webusername=tsajnani&webpassword=Capstone2017";
 
    // Create our ES2Web object.
    ES2Web web1 = new ES2Web(myURL + "&tag=tag");
      
    // Start downloading our data and wait for it to finish.
    yield return StartCoroutine(web1.Download());
      
    if(web1.isError)
    {
        // Enter your own code to handle errors here.
        Debug.LogError(web1.errorCode + ":" + web1.error);
    }
    else
    {
 
        // Or we could just load directly from the ES2Web object.
        Vector3 cubepos1 = web1.Load<Vector3>("tag");
		Load1(cubepos1);
    }
	Debug.Log("1");
}
	public void Load1(Vector3 cubepos1)
	{
		cube1.transform.position = cubepos1;
		Debug.Log("2");

	}
}