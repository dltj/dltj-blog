This Fedora-based repository interface, integrated with Sakai authorization,
will be capable of supporting a wide variety of data models. Different data 
models can be configured using XML Schema definitions, and presented using XSL 
Template files. The current implementation supports a strictly hierarchical 
data model, but more complex data models incorporating a Kowari triple-store 
ontology are possible. Data stored within the repository can be eventually 
transformed using custom dissemination methods as needed by Sakai collaboration
tools, and accessed via Twin Peaks.

The current implementation is a prototype, supporting browse, search and
editing capabilities. Authorization is not yet integrated with Sakai.
Error handling is rough, and the wish list is long.

Setup:

1. Setup Fedora 2.1 Server as defined at http://www.fedora.info
   Fedora should be configured to authorize access from the Sakai server.
   
2. Sakai server must have xerces 2.7.1 jar files installed in common/endorsed

3. Install the Lucene (http://lucene.apache.org/java/docs/index.html) and the 
   Generic Fedora Search Service (http://defxws2006.cvt.dk/fedoragsearch/). 
   Customizations are in the fgslucene sub-directory of this project.

4. The src/bundle/soapclient.properties file must be configured for the
   application-specific data model. The prototype will work "out of the box"
   with the sample data model, after configuring soapclient.properties with 
   the correct: fedora.host, fedoraServerUsername & fedoraServerPassword.
   
   Two sample applications are provided, with sample configurations
   in the soapclient.properties file. The data model is defined from
   the XML Schema files (src/webapp/xsd/*) and the presentation is defined
   in the XSLT files (src/web/xsl/*).
   
   
Data Model (XSD) Definition:
   
- must use the "xs" namespace prefix
- supported types include: xs:string, xs:date, xs:boolean, xs:integer,
                           xs:enumeration
- supported restrictions include: xs:maxLength
- xs:all and xs:sequence are supported; xs:choice is not (yet) supported
- xs:annotation is used to define human readable text for metadata entry forms

- Each XSD file should contain one (main) element definition, corresponding
  to one Fedora object type
- Each XSD file should define a title and description sub-element, which
  are duplicated in Fedora's dublin core metadata for possible OAI harvesting


XSL Template File Definition:

- Must include sakai_html_head and sakai_html_body_onload definitions
- must be wrapped in <div class="portletBody"> 

