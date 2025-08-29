using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ball : MonoBehaviour
{
    Ridigbody r;
    // Start is called before the first frame update
    
    {
        r = GetComponent<Ridigbody>();
    }

    // Update is called once per frame
    void Update()
    {
        float x = Input.GetAxis("Horizantal");
        float z = Input.GetAxis("Vertical");
        Vector3 f = new Vector3(x,0,z);
        r.AddForce(f*5);
    }
}
