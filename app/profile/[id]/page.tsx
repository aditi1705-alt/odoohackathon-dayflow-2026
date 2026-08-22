import { employees } from "@/lib/data";
import { notFound } from "next/navigation";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Card, CardContent } from "@/components/ui/card";

export default async function ProfilePage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const employee = employees.find((e) => e.id === id);

  if (!employee) return notFound();

  return (
    <div className="p-8 max-w-3xl mx-auto">
      <div className="flex items-center gap-4 mb-6">
        <Avatar className="h-20 w-20">
          <AvatarFallback className="text-xl">
            {employee.name.split(" ").map((n) => n[0]).join("")}
          </AvatarFallback>
        </Avatar>
        <div>
          <h1 className="text-2xl font-semibold">{employee.name}</h1>
          <p className="text-muted-foreground">{employee.designation}</p>
        </div>
      </div>

      <Tabs defaultValue="personal">
        <TabsList>
          <TabsTrigger value="personal">Personal</TabsTrigger>
          <TabsTrigger value="private">Private Info</TabsTrigger>
          {employee.role === "admin" && (
            <TabsTrigger value="salary">Salary Info</TabsTrigger>
          )}
          <TabsTrigger value="security">Security</TabsTrigger>
        </TabsList>

        <TabsContent value="personal">
          <Card><CardContent className="pt-6">
            <p>Designation: {employee.designation}</p>
            <p>Role: {employee.role}</p>
            <p>Status: {employee.status}</p>
          </CardContent></Card>
        </TabsContent>

        <TabsContent value="private">
          <Card><CardContent className="pt-6">
            <p className="text-muted-foreground">Address, phone, DOB go here.</p>
          </CardContent></Card>
        </TabsContent>

        {employee.role === "admin" && (
          <TabsContent value="salary">
            <Card><CardContent className="pt-6">
              <p className="text-muted-foreground">Salary breakdown goes here.</p>
            </CardContent></Card>
          </TabsContent>
        )}

        <TabsContent value="security">
          <Card><CardContent className="pt-6">
            <p className="text-muted-foreground">Password/security settings go here.</p>
          </CardContent></Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}