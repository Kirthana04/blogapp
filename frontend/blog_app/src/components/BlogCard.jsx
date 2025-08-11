import React from "react";
import { Link } from "react-router-dom";
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

// Component to display a single blog card
const BlogCard = ({ blog, id }) => {
  return (
    <Link to={`/blog/${id}`} className="hover:no-underline">
        {/* Card component to display blog details */}
      <Card className="hover:shadow-2xl translation-shadow curso h-full m-6 shadow-lg" style={{ backgroundColor: "var(--card-colour)" }}>
        
        {/* Card header with blog title */}
        <CardHeader>
          <CardTitle className="text-2xl font-serif " style={{color: "var(--header-background"}}>{blog.title}</CardTitle>
        </CardHeader>
        
        {/* Card content with blog description */}
        <CardContent>
          <p className="text-md text-muted-foreground break-words overflow-hidden text-ellipsis line-clamp-5 font-serif" style={{color: "var(--header-background"}}>
            {blog.content}
          </p>
        </CardContent>
       
        {/* Card footer with blog date */}
        <CardFooter className="text-xs text-muted-foreground" style={{color: "var(--header-background"}}>
          {blog.date}
        </CardFooter>
      </Card>
    </Link>
  );
};

export default BlogCard;
