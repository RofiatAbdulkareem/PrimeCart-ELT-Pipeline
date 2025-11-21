resource "aws_redshiftserverless_namespace" "elt-ns" {
  namespace_name = "elt-namespace"
}


resource "aws_redshiftserverless_workgroup" "elt-wg" {
  namespace_name = aws_redshiftserverless_namespace.elt-ns.namespace_name
  workgroup_name = "elt-wg"
}