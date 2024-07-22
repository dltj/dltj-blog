---
layout: wordpress-import
status: published
published: true
title: Java Application for Batch Processing FEDORA Objects
modified: 2018-01-15T22:38:08-05:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 150
wordpress_url: http://dltj.org/2006/12/fedora-batch-processing/
date: '2006-12-13 21:18:30 -0500'
date_gmt: '2006-12-14 02:18:30 -0500'
category: Library Technology
categories:
- Fedora
tags:
- java
- programming
- Fedora Repository
comments: []
---
We had a need today to transform an XML file with a custom DTD into Dublin Core; the custom XML file is a datastream in our [FEDORA repository][0] and we want to put the Dublin Core XML file back into the FEDORA object as the DC datastream. This took a slew of technologies and techniques: reading a datastream out of the FEDORA repository using [API-A][1], parsing XML documents using the [Java DOM library][2], creating a new document with the correct namespaces using Java DOM, and modifying the DC datastream in the repository using [API-M][3].

I'm posting the code here in case someone else might find it useful. Of course, if you know a better way please let me know. We'll probably need to do things like this again...

[0]: http://www.fedora.info/ "FEDORA Digital Object Repository homepage"
[1]: http://www.fedora.info/definitions/1/0/api/Fedora-API-A.html "FEDORA API-A WSDL Documentation"
[2]: http://java.sun.com/j2se/1.5.0/docs/api/org/w3c/dom/package-summary.html "org.w3c.dom (Java 2 Platform SE 5.0) documentation"
[3]: http://www.fedora.info/definitions/1/0/api/Fedora-API-M.html "FEDORA API-M WSDL Documentation"

```java
/**********************************************************************************
 *
 * Copyright (C) 2006 OhioLINK
 *
 * This file is part of the OhioLINK Digital Resource Commons (DRC) Project.
 *
 * The OhioLINK DRC is free software; you can redistribute it and/or
 * modify it under the terms of the Affero General Public License as
 * published by Affero, Inc. -- either version 1 of the License, or
 * (at your option) any later version.
 *
 * The OhioLINK DRC Project is distributed in the hope that it will be
 * useful, but WITHOUT ANY WARRANTY -- without even the implied warranty
 * of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * Affero General Public License for more details.
 *
 * You should have received a copy of the Affero General Public
 * License in the LICENSE.txt file that comes with the DRC project;
 * if not, write to DRC Development Team, OhioLINK, 2455 North Star Rd,
 * Suite 300, Columbus, OH 43221, USA.
 *********************************************************************************/

package batch;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.io.StringWriter;
import java.net.MalformedURLException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;

import fedora.client.FedoraClient;
import fedora.server.access.FedoraAPIA;
import fedora.server.management.FedoraAPIM;
import fedora.server.types.gen.DatastreamDef;
import fedora.server.types.gen.MIMETypedStream;

public class Batch {

 public static void main(String[] args) {
  for (int i = 80; i < 81; i++) {
   // "hdl" is our FEDORA PID prefix
   String pid = "hdl:" + i;

   try {
    FedoraClient client = new FedoraClient(
      "http://fedora.server/fedora",
      "fedoraAdmin", "password");
    FedoraAPIA apia = client.getAPIA();
    FedoraAPIM apim = client.getAPIM();
    
    //
    // Get the list of datastreams for this object.  For each one, we're
    // going to look for an identifier that ends in "etd"
    DatastreamDef[] datastreams = apia.listDatastreams(pid, null);
    for (int j = 0; j < datastreams.length; j++) {
     DatastreamDef def = datastreams[j];
     String itemId = def.getID();
     if (itemId.endsWith("etd")) {
      
      //
      // If we've found it, get it out of the FEDORA server and
      // create a XML DOM document for it
      MIMETypedStream ds = apia.getDatastreamDissemination(pid,itemId,null);
      byte[] file = ds.getStream();
      InputStream inputStream = new ByteArrayInputStream(file);
      // String fileStr = new String(file, "ascii");
      // System.out.println(fileStr);

      DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
      factory.setNamespaceAware(true);
      DocumentBuilder builder = factory.newDocumentBuilder();
      Document sourceDoc = builder.parse(inputStream);

      //
      // Now build an empty XML DOM document for the Dublin Core
      Document destDoc = builder.newDocument();
      Element rootElement=destDoc.createElementNS("http://www.openarchives.org/OAI/2.0/oai_dc/","oai_dc:dc");
      rootElement.setAttributeNS("http://www.w3.org/2000/xmlns/","xmlns:oai_dc","http://www.openarchives.org/OAI/2.0/oai_dc/");
      rootElement.setAttributeNS("http://www.w3.org/2000/xmlns/","xmlns:dc","http://purl.org/dc/elements/1.1/");
      destDoc.appendChild(rootElement);

      //
      // Now copy the values from the ETD XML document into
      // the DC XML document
      Element e; String value;
      e=destDoc.createElement("dc:identifier");
      e.appendChild(destDoc.createTextNode(pid));
      rootElement.appendChild(e);

      e=destDoc.createElement("dc:title");
      value=sourceDoc.getElementsByTagName("title").item(0).getTextContent().replaceAll("[\t ]*\n[\t ]*", " ").replaceAll("[\t ][\t ]+", " ").trim();
      e.appendChild(destDoc.createTextNode(value));
      rootElement.appendChild(e);
      
      // author's name comes in many parts; this'll put them together
      e = destDoc.createElement("dc:creator");
      String nameFields[] = { "authfname", "authmname", "authlname", "authsuffix"};
      String author = new String();
      for (String field : nameFields) {
       value = sourceDoc.getElementsByTagName(field).item(0).getTextContent().replaceAll("[\t ]*\n[\t ]*", " ").replaceAll("[\t ][\t ]+", " ").trim();
       if (value != null && !value.equals("")) {
        author = author.concat(value).concat(" ");
       }
      }
      e.appendChild(destDoc.createTextNode(author.trim()));
      rootElement.appendChild(e);       

      e=destDoc.createElement("dc:language");
      value=sourceDoc.getElementsByTagName("language").item(0).getTextContent().replaceAll("[\t ]*\n[\t ]*", " ").replaceAll("[\t ][\t ]+", " ").trim();
      e.appendChild(destDoc.createTextNode(value));
      rootElement.appendChild(e);

      e=destDoc.createElement("dc:description");
      value=sourceDoc.getElementsByTagName("abstract").item(0).getTextContent().replaceAll("[\t ]*\n[\t ]*", " ").replaceAll("[\t ][\t ]+", " ").trim();
      e.appendChild(destDoc.createTextNode(value));
      rootElement.appendChild(e);
      
      e=destDoc.createElement("dc:date");
      value=sourceDoc.getElementsByTagName("docyear").item(0).getTextContent().replaceAll("[\t ]*\n[\t ]*", " ").replaceAll("[\t ][\t ]+", " ").trim();
      e.appendChild(destDoc.createTextNode(value));
      rootElement.appendChild(e);       

      e=destDoc.createElement("dc:subject");
      value = sourceDoc.getElementsByTagName("subjects").item(0).getTextContent().replaceAll("[\t ]*\n[\t ]*", " ").replaceAll("[\t ][\t ]+", " ").trim();
      e.appendChild(destDoc.createTextNode(value));
      rootElement.appendChild(e);

      //
      // Use a Transformer for output
      TransformerFactory tFactory = TransformerFactory.newInstance();
      Transformer transformer = tFactory.newTransformer();
      transformer.setOutputProperty(javax.xml.transform.OutputKeys.OMIT_XML_DECLARATION, "yes");
      DOMSource source = new DOMSource(destDoc);
      StringWriter strWriter = new StringWriter();
      StreamResult result = new StreamResult(strWriter);
      transformer.transform(source, result);
      String xmlAsString=strWriter.getBuffer().toString();
      // System.out.println(xmlAsString);
      byte[] normalarr=xmlAsString.getBytes("UTF-8");
      
      //
      // Lastly, write the modified DC datastream back to the FEDORA server
      apim.modifyDatastreamByValue(pid, "DC", null, "Dublin Core", false, "text/xml", null, normalarr, "A", "Batch program to add DC datastream from ETD XML file", false);
     }
    }
   } catch (MalformedURLException e) {
    System.out.println(pid+" "+e.getLocalizedMessage());
   } catch (Exception e) {
    System.out.println(pid+" "+e.getLocalizedMessage());
   }
  }
 }
}
```
